from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_type


class TokenGenerator(PasswordResetTokenGenerator):
    def __make__hash__value(self, user, timestamp):
        return(
            text_type(user.pk) + text_type(timestamp)
        )

generate_token = TokenGenerator()