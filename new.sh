if [ "$#" -ne 3 ]
then
    echo "missing arguments"
    echo "useage:"
    echo "new.sh [language] yyyy dd"
    exit 1
fi

if [ -z "$2" -o -z "$3" ]
then 
    echo "arguments empty"
    echo "useage:"
    echo "new.sh [language] yyyy dd"
    exit 2
fi

if [ "$1" == "python" ]
then
    if [ -r "$2/python/day$3.py" ]
    then
        echo "error file already exists"
    else
        cp "templates/python.py" "$2/python/day$3.py"
        echo "$2/python/day$3.py"
    fi
elif [ "$1" == "rust" ]
then
    if [ -r "$2/rust-sln/src/day$3.rs" ]
    then
        echo "error file already exists"
    else
        cp "templates/rust.rs" "$2/rust-sln/src/day$3.rs"
        echo -e "\n[[bin]]\nname = \"day$3\"\npath = \"src/day$3.rs\"" >> "$2/rust-sln/Cargo.toml"
        echo "$2/rust-sln/src/day$3.rs"
    fi
else
    echo "unknown language"
    echo "useage:"
    echo "new.sh [language] yyyy dd"
fi


