from dataclasses import dataclass
from typing import NamedTuple


class Record(NamedTuple):
  conditions: str
  groups: tuple


def parse_line(line: str) -> Record:
  tokens = line.split()
  return Record(tokens[0], tuple([int(x) for x in tokens[1].split(',')]))


def parse_line2(line: str) -> Record:
  tokens = line.split()
  conditions = tokens[0] + '?' + tokens[0] + '?' + tokens[0] + '?' + tokens[0] + '?'+ tokens[0]
  return Record(conditions, tuple([int(x) for x in tokens[1].split(',')] * 5))


def matches(substring: str, conditions: str) -> bool:
  assert len(substring) <= len(conditions)
  for a,b in zip(substring, conditions):
    if b != '?' and a != b:
      return False
  return True


caches = dict()

def generate_possibilities(record: Record, intact_springs_to_distribute: int, index: int = 0, base_pattern: str = '') -> int:
  if index == len(record.groups):
    pattern = base_pattern + '.' * intact_springs_to_distribute
    if matches(pattern, record.conditions):
      return 1
    return 0
  is_at_edge = (index in (0, len(record.groups)))

  result = 0
  for distributed in range(intact_springs_to_distribute, -1, -1):
    pattern = base_pattern
    if not is_at_edge:
      pattern += '.'
    remaining_springs = intact_springs_to_distribute - distributed
    pattern += '.' * distributed
    if index < len(record.groups):
      pattern += '#' * record.groups[index]
    if matches(pattern, record.conditions):
      if record not in caches:
        caches[record]  = dict()
      cache = caches[record]
      args = (record, remaining_springs, index + 1)
      if args in cache:
        result += cache[args]
      else:
        cache[args] = generate_possibilities(record, remaining_springs, index + 1, pattern)
        result += cache[args]
      # result += generate_possibilities(record, remaining_springs, index + 1, pattern)
  return result
  

def process_record(record: Record) -> None:
  num_springs = len(record.conditions)
  num_damaged_springs = sum(record.groups)
  num_gaps = len(record.groups) - 1
  num_intact_springs = num_springs - num_damaged_springs - num_gaps
  
  return generate_possibilities(record, num_intact_springs)

# 1

# data = [parse_line(line) for line in open('../input/input12').read().splitlines()]

# total = 0
# for record in data:
#   total += process_record(record)
# print(total)

#2 

data = [parse_line2(line) for line in open('../input/input12').read().splitlines()]
total = 0
for record in data:
  total += process_record(record)
print(total)