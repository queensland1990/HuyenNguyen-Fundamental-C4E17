import pyexcel

data=[
    {
        "Name": "Huyen",
        "Age": 22
    },
    {
        "Name": "Huy",
        "Age": 23
    },
    {
        "Name": "An",
        "Age": 22
    },
]

pyexcel.save_as(records=data,dest_file_name="test.xlsx")
