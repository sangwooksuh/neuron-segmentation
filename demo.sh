#!/bin/bash
echo ""
echo "START DEMO"
echo "---"

echo "Learn usage:"
echo "---"
echo "$ python segment.py --help"
python segment.py --help
echo "---"

echo "Easy problem:"
echo "$ python segment.py ./data/easy"
python segment.py ./data/easy

echo "Evaluate score (IOU):"
echo "$ python evaluate.py ./data/easy 10"
echo "---"
python evaluate.py ./data/easy 10
echo "---"

echo "Medium problem with score (IOU):"
echo "$ python segment.py --neurons 2 --evaluate ./data/medium"
python segment.py --neurons 2 --evaluate ./data/medium

echo "Hard problem with score (IOU):"
echo "$ python segment.py --neurons 2 --evaluate ./data/hard"
python segment.py --neurons 2 --evaluate ./data/hard

echo "Oops! Try another threshold:"
echo "$ python segment.py --neurons 2 --threshold 0.5 --evaluate ./data/hard"
python segment.py --neurons 2 --threshold 0.5 --evaluate ./data/hard

echo "END DEMO"
echo ""
