from django.db import models


# Create your models here.
class Contact(models.Model):
    user_id=models.CharField(max_length=100)
    user_role=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.CharField(max_length=500)

class Process_complete(models.Model):
    contract_id = models.CharField(max_length=20, primary_key=True)
    CI_hash = models.CharField(max_length=100)
    SR_hash = models.CharField(max_length=100)
    LCR_hash = models.CharField(max_length=100)
    LC_hash = models.CharField(max_length=100)
    BL_hash = models.CharField(max_length=100)
    DO_hash = models.CharField(max_length=100)
    user1 = models.CharField(max_length=50)
    user2 = models.CharField(max_length=50)
    user3 = models.CharField(max_length=50)
    user4 = models.CharField(max_length=50)

class Process(models.Model):
    contract_id = models.CharField(max_length=20, primary_key=True)
    CI_hash = models.CharField(max_length=100)
    SR_hash = models.CharField(max_length=100)
    LCR_hash = models.CharField(max_length=100)
    LC_hash = models.CharField(max_length=100)
    BL_hash = models.CharField(max_length=100)
    DO_hash = models.CharField(max_length=100)
    user1 = models.CharField(max_length=50)
    user2 = models.CharField(max_length=50)
    user3 = models.CharField(max_length=50)
    user4 = models.CharField(max_length=50)


class Member(models.Model):
    user_role = models.CharField(max_length=20, primary_key=True)
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_pw = models.CharField(max_length=20)
    c_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.user_id


class Contract_LCR(models.Model):
    contractname = models.CharField(max_length=50)
    contract_id = models.CharField(max_length=20)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    Created = models.CharField(max_length=20,null=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)
    a = models.CharField(max_length=20,null=True)
    b = models.CharField(max_length=20,null=True)
    c = models.CharField(max_length=20,null=True)
    d = models.CharField(max_length=20,null=True)
    e = models.CharField(max_length=20,null=True)
    f = models.CharField(max_length=20,null=True)
    g = models.CharField(max_length=20,null=True)
    h = models.CharField(max_length=20,null=True)
    i = models.CharField(max_length=20,null=True)
    j = models.CharField(max_length=20,null=True)
    k = models.CharField(max_length=20,null=True)
    l = models.CharField(max_length=20,null=True)
    m = models.CharField(max_length=20,null=True)
    n = models.CharField(max_length=20,null=True)
    o = models.CharField(max_length=20,null=True)




class Contract_LC(models.Model):
    contractname = models.CharField(max_length=50,null=True)
    contract_id = models.CharField(max_length=20)
    sha256 = models.CharField(max_length=100,null=True)
    filename = models.CharField(max_length=100,null=True)
    Created = models.CharField(max_length=20,null=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100,null=True)
    share2 = models.CharField(max_length=100,null=True)
    share3 = models.CharField(max_length=100,null=True)
    share4 = models.CharField(max_length=100,null=True)
    a = models.CharField(max_length=20,null=True)
    b = models.CharField(max_length=20,null=True)
    c = models.CharField(max_length=20,null=True)
    d = models.CharField(max_length=20,null=True)
    e = models.CharField(max_length=20,null=True)
    f = models.CharField(max_length=20,null=True)
    g = models.CharField(max_length=20,null=True)
    h = models.CharField(max_length=20,null=True)
    i = models.CharField(max_length=20,null=True)
    j = models.CharField(max_length=20,null=True)
    k = models.CharField(max_length=20,null=True)
    l = models.CharField(max_length=20,null=True)
    m = models.CharField(max_length=20,null=True)
    n = models.CharField(max_length=20,null=True)
    o = models.CharField(max_length=20,null=True)
    p = models.CharField(max_length=20,null=True)
    q = models.CharField(max_length=20,null=True)
    r = models.CharField(max_length=20,null=True)
    s = models.CharField(max_length=20,null=True)
    t = models.CharField(max_length=20,null=True)
    u = models.CharField(max_length=20,null=True)
    v = models.CharField(max_length=20,null=True)
    w = models.CharField(max_length=20,null=True)
    x = models.CharField(max_length=20,null=True)
    y = models.CharField(max_length=20,null=True)
    z = models.CharField(max_length=20,null=True)
    aa = models.CharField(max_length=20,null=True)
    bb = models.CharField(max_length=20,null=True)
    cc = models.CharField(max_length=20,null=True)
    dd = models.CharField(max_length=20,null=True)
    ee = models.CharField(max_length=20,null=True)
    ff = models.CharField(max_length=20,null=True)
    gg = models.CharField(max_length=20,null=True)




class Contract_CI(models.Model):
    contractname = models.CharField(max_length=50)
    contract_id = models.CharField(max_length=20)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    Created = models.CharField(max_length=20, null=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)
    a = models.CharField(max_length=20,null=True)
    b = models.CharField(max_length=20,null=True)
    c = models.CharField(max_length=20,null=True)
    d = models.CharField(max_length=20,null=True)
    e = models.CharField(max_length=20,null=True)
    f = models.CharField(max_length=20,null=True)
    g = models.CharField(max_length=20,null=True)
    h = models.CharField(max_length=20,null=True)
    i = models.CharField(max_length=20,null=True)
    j = models.CharField(max_length=20,null=True)
    k = models.CharField(max_length=20,null=True)
    l = models.CharField(max_length=20,null=True)
    m = models.CharField(max_length=20,null=True)
    n = models.CharField(max_length=20,null=True)
    o = models.CharField(max_length=20,null=True)
    p = models.CharField(max_length=20,null=True)
    q = models.CharField(max_length=20,null=True)
    r = models.CharField(max_length=20,null=True)


class Contract_SR(models.Model):
    contractname = models.CharField(max_length=50)
    contract_id = models.CharField(max_length=20)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    Created = models.CharField(max_length=20, null=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)
    a = models.CharField(max_length=20,null=True)
    b = models.CharField(max_length=20,null=True)
    c = models.CharField(max_length=20,null=True)
    d = models.CharField(max_length=20,null=True)
    e = models.CharField(max_length=20,null=True)
    f = models.CharField(max_length=20,null=True)
    g = models.CharField(max_length=20,null=True)
    h = models.CharField(max_length=20,null=True)
    i = models.CharField(max_length=20,null=True)
    j = models.CharField(max_length=20,null=True)
    k = models.CharField(max_length=20,null=True)
    l = models.CharField(max_length=20,null=True)
    m = models.CharField(max_length=20,null=True)
    n = models.CharField(max_length=20,null=True)
    o = models.CharField(max_length=20,null=True)



class Contract_BL(models.Model):
    contractname = models.CharField(max_length=50)
    contract_id = models.CharField(max_length=20)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    Created = models.CharField(max_length=20, null=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)
    a = models.CharField(max_length=20,null=True)
    b = models.CharField(max_length=20,null=True)
    c = models.CharField(max_length=20,null=True)
    d = models.CharField(max_length=20,null=True)s
    e = models.CharField(max_length=20,null=True)
    f = models.CharField(max_length=20,null=True)
    g = models.CharField(max_length=20,null=True)
    h = models.CharField(max_length=20,null=True)
    i = models.CharField(max_length=20,null=True)
    j = models.CharField(max_length=20,null=True)


class Contract_DO(models.Model):
    contractname = models.CharField(max_length=50)
    contract_id = models.CharField(max_length=20)
    sha256 = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    Created = models.CharField(max_length=20, null=True)
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    share1 = models.CharField(max_length=100)
    share2 = models.CharField(max_length=100)
    share3 = models.CharField(max_length=100)
    share4 = models.CharField(max_length=100)
    a = models.CharField(max_length=20,null=True)
    b = models.CharField(max_length=20,null=True)
    c = models.CharField(max_length=20,null=True)
    d = models.CharField(max_length=20,null=True)
    e = models.CharField(max_length=20,null=True)
    f = models.CharField(max_length=20,null=True)
    g = models.CharField(max_length=20,null=True)