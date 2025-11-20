class Email:
    def __init__(self,id,title,description,time,status):
        self.id=id
        self.title=title
        self.description=description
        self.time=time
        self.status=status
EMAIL_STORE=[ Email(0,'Thông báo lịch phỏng vấn','Phỏng vấn lúc 14h tại phòng số 2','01/05/2025',False),
        Email(1,'Kết quả phỏng vấn','Chúc mừng bạn đã đậu phỏng vấn','04/05/2025',True),
        Email(2,'Thông báo lịch làm việc','8h hằng ngày từ thứ 2 đến thứ 6','08/05/2025',True)
        ]
def get_Email_list():
    return EMAIL_STORE

def get_Email_by_id(id):
    emails=get_Email_list()
    return emails[id]
def  delete_Email_by_id(id):
    global EMAIL_STORE
    EMAIL_STORE=[email for email in EMAIL_STORE if email.id != id]
def generate_new_id():
   
    if not EMAIL_STORE:
        return 1

    max_id = max(email.id for email in EMAIL_STORE)
    return max_id + 1


def add_new_email(title, description, time):
    global EMAIL_STORE
    new_id = generate_new_id()

    new_email = Email(new_id, title, description, time, False)
    

    EMAIL_STORE.append( new_email) 
    return new_email