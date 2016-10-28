import unittest
import json
from utils import *



def test_register_user():
    """
    register random user and verify response
    """
    authAccountId = generate_random_string()+"@gmail.com"
    password      = generate_random_string(9)
    name          = generate_random_string()
    r=register_user(authAccountId,password,name,True)
    assert len(json.loads(r.text).keys()) <= 2,"extrat fields present in the register user API call response"
    assert "userId" in json.loads(r.text).keys(), "no userId in the register user API call response"
    assert "sessionId" in json.loads(r.text).keys(),'no sessionId in register user API call response'

def test_authorize_set_cookies():
    """
    register a new user than authorize it using the authorize user API call
    and check the response
    """
    authAccountId = generate_random_string()+"@gmail.com"
    password      = generate_random_string(9)
    name          = generate_random_string()
    register_user(authAccountId,password,name,False)
    r=authorize_set_cookies(authAccountId,password,True)
    assert len(json.loads(r.text).keys()) <= 2,"extrat fields present in the register user API call response"
    assert "userId" in json.loads(r.text).keys(), "no userId in the register user API call response"
    assert "sessionId" in json.loads(r.text).keys(),'no sessionId in register user API call response'

def test_get_user_profile():
    """
    register a new user than get it's profile using the API call
    """
    authAccountId = generate_random_string()+"@gmail.com"
    password      = generate_random_string(9)
    name          = generate_random_string()
    r=register_user(authAccountId,password,name,False)
    userId = json.loads(r.text)['userId']
    r=get_user_profile(userId)
    assert 'id' in json.loads(r.text).keys() ,"no id in the get_user_profile API response"
    assert 'accountId' in json.loads(r.text).keys(),"no accountId in the get_user_profile API response"
    assert 'handle' in json.loads(r.text).keys(),"no handle in the get_user_profile API response"
    assert 'fullName' in json.loads(r.text).keys(),"no fullName in the get_user_profile API response"
    assert 'avatarId' in json.loads(r.text).keys(),"no avatarId in the get_user_profile API response"
    assert 'about' in json.loads(r.text).keys(),"no about in the get_user_profile API response"
    assert 'creationTime' in json.loads(r.text).keys(),"no creationTime in the get_user_profile API response"
    assert 'roles' in json.loads(r.text).keys(),"no roles in the get_user_profile API response"
    assert len(json.loads(r.text).keys()) <= 8,"extrat fields present in the get_user_profile API response"

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


"""
def test_isItBeforeSpecificWord():
	assert isItBeforeSpecificWord("word","specificWord",["word","specificWord"])


def test_isItAfterSpecificWord():
	assert isItAfterSpecificWord("word","specificWord",["specificWord","word"]), "isItAfterSpecificWord function failed in positive test"
	assert not isItAfterSpecificWord("word","specificWord",["notASpecificWord","word"]),"isItAfterSpecificWord function failed in negative test"


def test_isItBeforeAwordThatStartsWithANumber():
	assert isItBeforeAwordThatStartsWithANumber("word",["word","1startsWithIt"])
	assert not isItBeforeAwordThatStartsWithANumber("word",["word","startsWithOut1"])


def test_isItAfterAwordThatStartsWithANumber():
	assert isItAfterAwordThatStartsWithANumber("word",["1startsWithIt","word"])
	assert not isItAfterAwordThatStartsWithANumber("word",["word","startsWithOut1"])

def test_isItSignificantWord():
	assert isItSignificantWord("dog")
	assert not isItSignificantWord("iplsg")

def test_isItStartsWithANumber():
	assert isItStartsWithANumber("1startwithANumber")
	assert not isItStartsWithANumber("NotStartinwith1Number")

def test_doesItContainANumber():
	assert doesItContainANumber("h4tt")
	assert not doesItContainANumber("NoNumber")

def test_isItContainOneWord():
	assert isItContainOneWord("word")
	assert not isItContainOneWord("two words")

def test_doesItStartsWithUpperCase():
	assert doesItStartsWithUpperCase("Yes")
	assert not doesItStartsWithUpperCase("no")

def test_isItANoun():
	assert isItANoun("door","open the door")
	assert not isItANoun("open","open the door")

def test_isItANAdj():
	assert isItANAdj("good","good boy")
	assert not isItANAdj("boy","good boy")

def test_isItAVerb():
	assert isItAVerb("go","go to the home")
	assert not isItAVerb("home","go to the home")
"""
