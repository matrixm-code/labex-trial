#!/bin/zsh
python -c "import json;result=json.load(open('/home/labex/project/list.json', 'r'));answer=[[i%(j+1) for j in range(10)] for i in range(50)];assert len(result)==len(answer);assert all(a in result for a in answer);"
