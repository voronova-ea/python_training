Scenario Outline: Add new contact
  Given a contact list
  Given a contact with new <firstname>, <lastname>, <address>, <home> and <mobile> values
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact


  Examples:
  | firstname  | lastname  | address  | home   | mobile |
  |            |           |          |        |        |
  | firstname1 | lastname1 | address1 | 222222 | 111111 |
  | firstname2 | lastname2 | address2 | 333333 | 222222 |
  |            | 123       |          |        |        |


Scenario Outline: Edit contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with new <firstname>, <lastname>, <address>, <home> and <mobile> values
  When I edit fields of the random contact to new values
  Then the new contact list is equal to the old list with the edited contact


  Examples:
  | firstname  | lastname  | address  | home   | mobile |
  |            |           |          |        |        |
  | first1     | last1     | add1     | 444444 | 555555 |
  | firstname2 | lastname2 | address2 | 333333 | 222222 |
  | abc        |           |          | 123    |        |


Scenario Outline: Delete contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact