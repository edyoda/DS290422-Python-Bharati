data = {
    "python_batch":{
            "students":{
                "name":"Mahek",
                "rno":1,
                "marks":{
                    "logical":30,
                    "technical":40,
                    "practical":50
                }
            }
        }
    }

print(data["python_batch"]['students']['marks']['practical'])
