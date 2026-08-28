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

    student_keyz=[student_details["name"],student_details["country"]]
    if student_keyz not in seen_keys:
        seen_keys.append(student_keyz)
        result_dict[student_id]=student_keyz

print(result_dict)