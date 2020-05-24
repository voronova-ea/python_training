*** Setting ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname1  lastname1  address1  222222  111111
    Create Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}


Edit contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact_data}=  New Contact Data  ${index}  firstname1  lastname1  address1  222222  111111
    ${contact}=  Get From List  ${old_list}  ${index}
    Edit Contact  ${contact}  ${contact_data}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Append To List  ${old_list}  ${contact_data}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}


Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}