import json
from .models import Form
def form_edit_create(request, pk):
    data = json.loads(request.body)
    error_list = []

    name =data.get("username")             #didnot get keyerror if you use get
    if not name:
        error_list.append("Username cannot be empty")

    address =data.get("address")    #bahira bata aako data () ma huncha  
    if not address:
        error_list.append("Address cannot be empty")

    contact =data.get("contact")
    if not contact:
        error_list.append("Contact cannot be empty.")
    else:
        if pk:#pk for update
            if Form.objects.filter(contact=contact).exclude(id=pk).exists():
                error_list.append("Mobile number already exists")
        else:
             if Form.objects.filter(contact=contact).exists():
                error_list.append("Mobile number already exists")

    email =data.get("email")
    if not email:
        error_list.append("Email cannot be empty")
    else:
        if pk:
            if Form.objects.filter(email=email).exclude(id=pk).exists():
                error_list.append("Email already exists")
        else:
            if Form.objects.filter(email=email).exists():
                error_list.append("Email already exists")

    return error_list, name, address, contact, email

