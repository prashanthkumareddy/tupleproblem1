def convert_tuple(tup):
    result=''
    for item in tup:
        result += item
    return result

my_tuple=('p','y','t','h','o','n')
convert_str_to_tuple=convert_tuple(my_tuple)
print(convert_str_to_tuple)