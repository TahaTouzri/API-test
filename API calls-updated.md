Initial notes
-------------

Simple request to register user:
curl https://beta.1neschool.com/core/users -v -H "Content-Type: application/json" -d '{"authType": "DbAuthTypeInternal", "authAccountId":"test@example.com", "password":"some password", "name": "Test User", "remember": false}'

Super admin credentials:
authAccountId: admin@hamoye.com
password: BQ4AT&i+o9B?zqUAVPwYUVEDcCLBsUZoDR

Option[] container means that corresponding field may be missing.

There is no additional text for errors for now, therefore error codes
should be used to distinguish different cases.

If you see error like "Foo isn't valid value for DbBar", you should
try using "DbBarFoo" as input.

If you're getting cryptic responses, try gunzipping them.

Known issues:
- authType should be equal to "Internal" when used as the part of URL, but "DbAuthTypeInternal"
  when used inside request body;
- ticket language detection is disabled for now;


API calls
---------













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

GET /tickets/{ticketId}
=======================

Request fields:
ticketId: String -- id of ticket to be retrieved

Gets support ticket. May be requested only by SuperAdmin, Admin, SuperModerator or
Moderator.

Response fields:
title: String
description: String
creationTime: DateTime -- time ticket was created
updateTime: DateTime -- time ticket was last time updated
priority: String -- ticket priority, one of DbTicketPriority(Low|Medium|High)
state: String -- ticket state, one of DbTicketState(Open|Closed)
language: Option[String] -- ticket language (autodetected)
assignedTo: Option[User] -- user this ticket is assigned to
