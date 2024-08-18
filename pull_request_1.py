import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")        

complete_detail = response.json()

values_a = [(d["id"], d["user"]) for d in complete_detail]           #to print the multiple key for all users
#"user" is another key which consists of dictionary  {dictionary {dictionary inside another dictionary}}

# for i in range(len(complete_detail)):                   # to print the single key like "id" of all users
#     # print(complete_detail[0]["id"])                   # to print the single key of zeroth user
#     # print(complete_detail[i]["user"]["login"])
#     print(complete_detail[i]["id"])

print(values_a)