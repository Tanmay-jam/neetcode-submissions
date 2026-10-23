class Solution:
    def processed(self, email):
        mail_parts = email.split("@")
        mail_parts[0] = mail_parts[0].replace('.','')
        mail_parts[0] = mail_parts[0].split('+')[0]
        return mail_parts[0] + '@' + mail_parts[1]

    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            emails[i] = self.processed(emails[i])
        return len(set(emails))
