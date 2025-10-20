class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        hashSet=set()
        for email in emails:
            local=email[:email.index('@')]
            domain=email[email.index('@')+1:]

            local=local.replace('.','')
            if '+' in local:
                local=local[:local.index('+')]
            hashSet.add(f"{local}@{domain}")
        return len(hashSet)
        