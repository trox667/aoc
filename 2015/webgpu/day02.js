export function createBufferInit(
  device,
  descriptor,
) {
  const contents = new Uint8Array(descriptor.contents);

  const unpaddedSize = contents.byteLength;
  const padding = 4 - (unpaddedSize % 4);
  const paddedSize = padding + unpaddedSize;

  const buffer = device.createBuffer({
    label: descriptor.label,
    usage: descriptor.usage,
    mappedAtCreation: true,
    size: paddedSize,
  });
  const data = new Uint8Array(buffer.getMappedRange());
  data.set(contents);
  buffer.unmap();
  return buffer;
}

export async function part1(
  input,
) {
  const adapter = await navigator.gpu.requestAdapter({
    powerPreference: "high-performance",
  });
  const device = await adapter?.requestDevice();
  if (!device) {
    return -1;
  }

  const WORKGROUP_Y = 1;
  const WORKGROUP_Z = 1;



  const inputArrayBuffer = input;
  const outputArrayBuffer = new Int32Array(2).fill(0);

  const inputStorageBuffer = createBufferInit(device, {
    label: "INPUT BUFFER",
    usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_DST,
    contents: inputArrayBuffer.buffer,
  });

  const outputStorageBuffer = createBufferInit(device, {
    label: "OUTPUT BUFFER",
    usage: GPUBufferUsage.STORAGE | GPUBufferUsage.COPY_DST |
      GPUBufferUsage.COPY_SRC,
    contents: outputArrayBuffer.buffer,
  });

  const stagingBuffer = device.createBuffer({
    size: outputArrayBuffer.byteLength,
    usage: GPUBufferUsage.MAP_READ | GPUBufferUsage.COPY_DST,
  });

  const shaderCode = `
  struct Result {
    partOne: atomic<i32>,
    partTwo: atomic<i32>,
  };

  @group(0)
  @binding(0)
  var<storage, read> input: array<i32>;

  @group(0)
  @binding(1)
  var<storage, read_write> result: Result;

  @compute
  @workgroup_size(1, 1, 1)
  fn main(@builtin(global_invocation_id) global_id: vec3<u32>) {

    if (global_id.x > ${input.length}u) {
      return;
    }

    let startIdx = global_id.x;
    // surface
    let w = input[startIdx*3];
    let h = input[startIdx*3+1];
    let l = input[startIdx*3+2];
    let a = w*h;
    let b = w*l;
    let c = h*l;
    let d = min(a, min(b,c));
    
    atomicAdd(&result.partOne, 2*a+2*b+2*c+d);

    // ribbon
    let volume = w*h*l;
    let aa = w+h;
    let bb = w+l;
    let cc = h+l;
    let dd = 2 * min(aa, min(bb, cc));
    atomicAdd(&result.partTwo, dd + volume);
  }
  `;

  const shaderModule = device.createShaderModule({
    code: shaderCode,
  });

  // const bindGroupLayout = computePipeline.getBindGroupLayout(0);
  const bindGroupLayout = device.createBindGroupLayout({
    entries: [
      {
        binding: 0,
        visibility: GPUShaderStage.COMPUTE,
        buffer: {
          type: "read-only-storage",
        },
      },
      {
        binding: 1,
        visibility: GPUShaderStage.COMPUTE,
        buffer: {
          type: "storage",
        },
      },
    ],
  });

  const computePipeline = device.createComputePipeline({
    layout: device.createPipelineLayout({
      bindGroupLayouts: [bindGroupLayout],
    }),
    compute: {
      module: shaderModule,
      entryPoint: "main",
    },
  });
  const bindGroup = device.createBindGroup({
    layout: bindGroupLayout,
    entries: [
      {
        binding: 0,
        resource: { buffer: inputStorageBuffer },
      },
      {
        binding: 1,
        resource: { buffer: outputStorageBuffer },
      },
    ],
  });

  const encoder = device.createCommandEncoder();
  const computePass = encoder.beginComputePass();
  computePass.setPipeline(computePipeline);
  computePass.setBindGroup(0, bindGroup);
  computePass.dispatchWorkgroups(
    input.length / 3
  );
  computePass.end();

  encoder.copyBufferToBuffer(
    outputStorageBuffer,
    0,
    stagingBuffer,
    0,
    outputArrayBuffer.byteLength,
  );
  const t0 = performance.now();
  device.queue.submit([encoder.finish()]);

  await stagingBuffer.mapAsync(GPUMapMode.READ);
  const arrayBufferData = stagingBuffer.getMappedRange();
  const intData = new Int32Array(arrayBufferData);
  const partOne = intData[0];
  const partTwo = intData[1];
  stagingBuffer.unmap();
  console.log(`GPU computation took ${performance.now() - t0}ms`);
  return [partOne, partTwo];
}

fetch("./input02").then(response => response.text()).then(async text => {
  const input = text.split("\n");
  const arr = new Int32Array(input.length * 3).fill(0);
  for (let i = 0; i < input.length; ++i) {
    const tokens = input[i].split("x").map(token => parseInt(token))
    arr[i * 3] = tokens[0]
    arr[i * 3 + 1] = tokens[1]
    arr[i * 3 + 2] = tokens[2]
  }

  const result = await part1(arr)
  console.log(result)

})

// const input = "2x3x4\n1x1x10".split("\n")

// const arr = new Int32Array(input.length * 3).fill(0);
// for (let i = 0; i < input.length; ++i) {
//   const tokens = input[i].split("x").map(token => parseInt(token))
//   arr[i * 3] = tokens[0]
//   arr[i * 3 + 1] = tokens[1]
//   arr[i * 3 + 2] = tokens[2]
// }
// console.log(arr)

// const result = await part1(arr)
// console.log(result)