from database_dump import *
from gmail_attach import *

if __name__ == "__main__":
    test = MailAgent()
    test.displayInfo("unseen")
    test.getAttachment("unseen")
    main()