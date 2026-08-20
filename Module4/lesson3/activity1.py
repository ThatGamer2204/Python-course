student_data={
    2018903:{"name":"Saket","country":"India"},
    2014129:{"name":"Alson","country":"Nepal"},
    2017783:{"name":"Sachinda","country":"Srilanka"}
}
print(student_data)
result_dict={}
seen_keys=[]
for student_id,student_details in student_data.items():
    print(student_id, "and ",student_details["name"], "and ",student_details["country"])