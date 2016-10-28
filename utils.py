import requests
import json
import string
import random
#-------------------------------------------------------------------------------
#                        register_user
#-------------------------------------------------------------------------------
def register_user(authAccountId,password,name,remember):
    """
    POST /core/users
    ================

    Request fields:
    authType: String -- should be equal to "DbAuthTypeInternal"
    authAccountId: String -- user's email
    password: Option[String] -- user's password, longer than 6 characters
    name: Option[String] -- user's full name
    remember: Boolean -- true to set permanent cookie

    Registers user and sets session cookie. Does not require authorization.

    Response fields:
    userId: String -- id of newly created user
    sessionId: String -- id of newly created session
    """
    url = "https://beta.1neschool.com/core/users"
    headers = {'Content-Type': u"application/json"}
    data ={'authType':'DbAuthTypeInternal',
           'authAccountId':authAccountId,#'ttaha@gmail.com',
           'password': password,#'tahataha',
           'name':name,#'Taha',
           'remember': remember#False
           }
    data = json.dumps(data)

    r=requests.post(url,headers=headers,data=data)
    return r
#-------------------------------------------------------------------------------
#                        authorize_set_cookies
#-------------------------------------------------------------------------------
def authorize_set_cookies(authAccountId,password,rememeber):
    """
    POST /acl/auth/{authType}/{authAccountId}
    =========================================

    Request fields:
    password: Option[String] -- user's password

    Authorizes user and sets session cookie.

    Response fields:
    userId: String -- id of newly created user
    sessionId: String -- id of newly created session
    """
    url = "https://beta.1neschool.com/acl/auth/Internal/"+authAccountId
    headers = {'Content-Type': u"application/json"}
    data ={
           'password': password,#'tahataha',
           'remember':rememeber
           }
    data = json.dumps(data)
    r=requests.post(url,headers=headers,data=data)
    return r

#-------------------------------------------------------------------------------
#                                      get_user_profile
#-------------------------------------------------------------------------------
def get_user_profile(id):
    """
    GET /core/users/{id}
    ====================

    Returns user's profile information. Does not require authorization.

    Response fields:
    id: String -- user's id
    accountId: String -- user's email for Internal auth, external account id for OAuth
    handle: Option[String] -- user's handle
    fullName: String
    avatarId: Option[String] -- link to avatar
    about: String -- profile description
    creationTime: org.joda.time.DateTime -- profile creation time
    roles: Array[String] -- information about user's privileges
    """
    url = "https://beta.1neschool.com/core/users/"+id
    r=requests.get(url)
    return r

#-------------------------------------------------------------------------------
#                                      update_profile_description
#-------------------------------------------------------------------------------

def update_profile_description():
    """
    PATCH /core/users/{id}
    ======================

    Request fields:
    about: String -- updates profile description
    fullName: String
    avatarId: String -- updates avatar

    Updates user profile. User can update only their own profile.
    """
    url = "https://beta.1neschool.com/core/users/0afb5bcb02111000"
    headers = {'Content-Type': u"application/json"}
    data ={'about':'update my profile',
           'fullName':'Taha',
           'handle': 'firstupdatetitan',
           'avatarId':'update'
           }
    data = json.dumps(data)

    r=requests.patch(url,headers=headers,data=data)
    return r
#-------------------------------------------------------------------------------
#                        grant_role_to_user
#-------------------------------------------------------------------------------
def grant_role_to_user(id,role):
    """
    POST /acl/users/{id}/roles
    ==========================

    Request fields:
    role: String -- role to be granted to user

    Grants specific role to user. Currently available roles are SuperAdmin, Admin,
    SuperModerator, Moderator, TechnicalSupport, SchoolAdmin, ServiceProvider, Customer.
    Only SuperAdmin can grant SuperAdmin and Admin roles. Both Admins, SuperAdmins and
    SuperModerators can grant Moderator and TechnicalSupport roles. SuperModerator,
    SchoolAdmin, ServiceProvider and Customer roles can be granted only by Admin and
    SuperAdmin.
    """
    url = "https://beta.1neschool.com/acl/users/"+id+"/roles"
    headers = {'Content-Type': u"application/json"}
    data ={'role':role}
    data = json.dumps(data)
    r=requests.post(url,headers=headers,data=data)

    return r

#-------------------------------------------------------------------------------
#                        test 5
#-------------------------------------------------------------------------------
def revoke_role_from_user(id,role):
    """
    DELETE /acl/users/{id}/roles
    ============================
    Request fields:
    role: String -- role to be revoked from user
    Revokes specific role from user. Revoke rights are the same as the grant role ones.
    """
    url = "https://beta.1neschool.com/acl/users/"+id+"/roles"
    headers = {'Content-Type': u"application/json"}
    data ={'role':role}
    data = json.dumps(data)
    r=requests.delete(url,headers=headers,data=data)

    return r

#-------------------------------------------------------------------------------
#                        test 5
#-------------------------------------------------------------------------------
def create_ticket(title,description,ticket_type):
    """
    POST /tickets
    =============

    Request fields:
    title: String -- ticket's title
    discription: String -- ticket's description
    type: String -- one of DbTicketType(SupportTicket|TypeBugReport|FeedbackTicket)

    Creates support ticket. May be requested by any user. Default behaviour
    assigns tickets to Moderators and SuperModerators (if there are no regular ones).

    Response fields:
    ticketId: String -- id of newly created ticket
    """
    url = "https://beta.1neschool.com/tickets"
    headers = {'Content-Type': u"application/json"}
    data ={'title':title,
    'description':description,
    '`type`':ticket_type
    }
    data = json.dumps(data)
    r=requests.post(url,headers=headers,data=data)
    return r
#print regester_user("tata@gmail.com","tahataha","taha",True)
#print authorize_set_cookies("tata@gmail.com","tahataha",True)
#print get_user_profile("0afd64b37b111000")

#-------------------------------------------------------------------------------
#                                 generate random string
#-------------------------------------------------------------------------------
def generate_random_string(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

"""
print authorize_set_cookies("admin@hamoye.com","BQ4AT&i+o9B?zqUAVPwYUVEDcCLBsUZoDR",True)
print get_user_profile("0afd64b37b111000")
print grant_role_to_user("0afd64b37b111000","SchoolAdmin")
print revoke_role_from_user("0afd64b37b111000","SchoolAdmin")
"""
#create_ticket("test ticket","test test ","SupportTicket")
#print generate_random_string()
