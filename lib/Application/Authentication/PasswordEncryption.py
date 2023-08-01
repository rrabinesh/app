# <?php

# class PasswordEncryption
# {
#     /**
#      * @internal only for testing, use EncryptPassword
#      * @param $password
#      * @param $salt
#      * @return string
#      */
#     public function Encrypt($password, $salt)
#     {
#         return sha1($password . $salt);
#     }

#     /**
#      * @param $plainTextPassword string
#      * @return EncryptedPassword
#      */
#     public function EncryptPassword($plainTextPassword)
#     {
#         $salt = $this->Salt();

#         $encrypted = $this->Encrypt($plainTextPassword, $salt);
#         return new EncryptedPassword($encrypted, $salt);
#     }

#     public function Salt()
#     {
#         return substr(str_pad(dechex(mt_rand()), 8, '0', STR_PAD_LEFT), -8);
#     }
# }

# class RetiredPasswordEncryption
# {
#     public function Encrypt($password)
#     {
#         return md5($password);
#     }
# }

# class EncryptedPassword
# {
#     /**
#      * @var string
#      */
#     private $encryptedPassword;

#     /**
#      * @var string
#      */
#     private $salt;

#     /**
#      * @param $encryptedPassword string
#      * @param $salt string
#      */
#     public function __construct($encryptedPassword, $salt)
#     {
#         $this->encryptedPassword = $encryptedPassword;
#         $this->salt = $salt;
#     }

#     /**
#      * @return string
#      */
#     public function EncryptedPassword()
#     {
#         return $this->encryptedPassword;
#     }

#     /**
#      * @return string
#      */
#     public function Salt()
#     {
#         return $this->salt;
#     }
# }


# PasswordEncryption class (Implementation for encryption)
class PasswordEncryption:
    def encrypt(self, password: str, salt: str) -> str:
        return sha1((password + salt).encode()).hexdigest()

    def encrypt_password(self, plain_text_password: str) -> "EncryptedPassword":
        salt = self.salt()
        encrypted = self.encrypt(plain_text_password, salt)
        return EncryptedPassword(encrypted, salt)

    def salt(self) -> str:
        return "{:08x}".format(random.getrandbits(32))


# RetiredPasswordEncryption class (Implementation for retired password encryption)
class RetiredPasswordEncryption:
    def encrypt(self, password: str) -> str:
        return md5(password.encode()).hexdigest()


# EncryptedPassword class
class EncryptedPassword:
    def __init__(self, encrypted_password: str, salt: str):
        self.encrypted_password = encrypted_password
        self.salt = salt

    def encrypted_password(self) -> str:
        return self.encrypted_password

    def salt(self) -> str:
        return self.salt

