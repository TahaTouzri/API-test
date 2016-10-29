import unittest
import json
from utils import *





class test_api():
    def __init__(self):
        self.title     = ""
        self.purpose   = ""
        self.test_pass = False
        self.steps     = []
    def add_step(self,step):
        # step: list like: [step_purpose,step_pass,message]
        self.steps.append({'step_purpose':step[0],'step_pass':step[1],'message':step[2]})
    def get_test_result(self):
        self.test_pass = True
        for step in self.steps:
            if not step['step_pass']:
                self.test_pass = False
        return self.test_pass
    def __str__(self):
        prt="+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        prt+= "title: "+self.title+"\n"
        prt+="test pass: "+str(self.get_test_result())+"\n"
        prt+= "purpose: "+self.purpose+"\n"
        prt+="+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        for step in self.steps:
            prt+= "purpose: "+step['step_purpose']+"\n"
            prt+= "step pass: "+str(step['step_pass'])+"\n"
            prt+= "message: "+step['message']+"\n"
            prt+="-----------------------------------------------------------\n"
        return prt

def test_register_user():
    """
    register random user and verify response
    """
    test_reg_user = test_api()
    test_reg_user.title = "Registe User API call"
    test_reg_user.purpose = "Test the call response format"
    #---------------------------------------------------------------------------
    #                     initialise test
    #--------------------------------------------------------------------------
    authAccountId = generate_random_string()+"@gmail.com"
    password      = generate_random_string(9)
    name          = generate_random_string()
    r=register_user(authAccountId,password,name,True)
    #---------------------------------------------------------------------------
    step_purpose = "verify that the response is in json format"
    step_pass    = False
    message = ""
    try:
        response = json.loads(r.text)
        message  = str(r.text)
        test_reg_user.add_step([step_purpose,True,message])
    except ValueError:
        message = str(r.text)
        test_reg_user.add_step([step_purpose,False,message])
        return test_reg_user
    #---------------------------------------------------------------------------
    step_purpose = "verify that there is no extrat fields in the response"
    step_pass    = True
    message = str(response.keys())
    if len(response.keys())>2:
        step_pass = False
        message = "extrat fields present in the register user API call response: "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that userId present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("userId" in response.keys()):
        test_pass = False
        message   = "no userId in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that sessionId present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("sessionId" in response.keys()):
        test_pass = False
        message   = "no sessionId in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    return test_reg_user




def test_authorize_set_cookies():
    """
    register a new user than authorize it using the authorize user API call
    and check the response
    """
    test_reg_user = test_api()
    test_reg_user.title = "authorize_set_cookies API call"
    test_reg_user.purpose = "Test the call response format"
    #---------------------------------------------------------------------------
    #                     initialise test
    #--------------------------------------------------------------------------
    authAccountId = generate_random_string()+"@gmail.com"
    password      = generate_random_string(9)
    name          = generate_random_string()
    register_user(authAccountId,password,name,False)
    r=authorize_set_cookies(authAccountId,password,True)
    #---------------------------------------------------------------------------
    step_purpose = "verify that the response is in json format"
    step_pass    = False
    message = ""
    try:
        response = json.loads(r.text)
        message  = str(r.text)
        test_reg_user.add_step([step_purpose,True,message])
    except ValueError:
        message = str(r.text)
        test_reg_user.add_step([step_purpose,False,message])
        return test_reg_user
    #---------------------------------------------------------------------------
    step_purpose = "verify that there is no extrat fields in the response"
    step_pass    = True
    message = str(response.keys())
    if len(response.keys())>2:
        step_pass = False
        message = "extrat fields present in the register user API call response: "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that userId present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("userId" in response.keys()):
        test_pass = False
        message   = "no userId in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that sessionId present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("sessionId" in response.keys()):
        test_pass = False
        message   = "no sessionId in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    return test_reg_user



def test_get_user_profile():
    """
    register a new user than get it's profile using the API call
    """
    test_reg_user = test_api()
    test_reg_user.title = "authorize_set_cookies API call"
    test_reg_user.purpose = "Test the call response format"
    #---------------------------------------------------------------------------
    #                     initialise test
    #--------------------------------------------------------------------------
    authAccountId = generate_random_string()+"@gmail.com"
    password      = generate_random_string(9)
    name          = generate_random_string()
    r=register_user(authAccountId,password,name,False)
    userId = json.loads(r.text)['userId']
    r=get_user_profile(userId)
    #---------------------------------------------------------------------------
    step_purpose = "verify that the response is in json format"
    step_pass    = False
    message = ""
    try:
        response = json.loads(r.text)
        message  = str(r.text)
        step_pass = True
        test_reg_user.add_step([step_purpose,step_pass,message])
    except ValueError:
        message = str(r.text)
        test_reg_user.add_step([step_purpose,step_pass,message])
        return test_reg_user
    #---------------------------------------------------------------------------
    step_purpose = "verify that there is no extrat fields in the response"
    step_pass    = True
    message = str(response.keys())
    if len(response.keys())>8:
        step_pass = False
        message = "extrat fields present in the register user API call response: "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that id present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("id" in response.keys()):
        step_pass = False
        message   = "no id in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that accountId present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("accountId" in response.keys()):
        step_pass = False
        message   = "no accountId in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that handle present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("handle" in response.keys()):
        step_pass = False
        message   = "no handle in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that fullName present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("fullName" in response.keys()):
        step_pass = False
        message   = "no fullName in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that avatarId present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("avatarId" in response.keys()):
        step_pass = False
        message   = "no avatarId in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that about field present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("about" in response.keys()):
        step_pass = False
        message   = "no about in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that creationTime field present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("creationTime" in response.keys()):
        test_pass = False
        message   = "no creationTime in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    #---------------------------------------------------------------------------
    step_purpose = "verify that roles field present in the response"
    step_pass    = True
    message = str(response.keys())
    if not ("roles" in response.keys()):
        test_pass = False
        message   = "no roles in "+str(response.keys())
    test_reg_user.add_step([step_purpose,step_pass,message])
    return test_reg_user




def test_grant_role_to_user():
    # create new user
    authAccountId = generate_random_string()+"@gmail.com"
    password      = generate_random_string(9)
    name          = generate_random_string()
    r=register_user(authAccountId,password,name,False)
    id=json.loads(r.text)['userId']
    #authenticate as superadmin
    authorize_set_cookies("admin@hamoye.com","BQ4AT&i+o9B?zqUAVPwYUVEDcCLBsUZoDR",True)
    r=grant_role_to_user(id,"ServiceProvider")
    assert r.text=="success","no reponse is given in the specification for the grantUserAPI call, we get"+r.text

def test_create_ticket():
    r=create_ticket("title","description","TypeBugReport")
    assert  'ticketId' in json.loads(r.text).keys(),"no roles in the get_user_profile API response"


print test_register_user()
print test_authorize_set_cookies()
print test_get_user_profile()
