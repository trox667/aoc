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
else
    echo "unknown language"
    echo "useage:"
    echo "new.sh [language] yyyy dd"
fi
