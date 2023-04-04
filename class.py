class Shaxs:
    def __init__(self, ism, familiya, t_yil):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.otasi = ''

    def get_FIO(self):
        info = f"{self.ism} {self.familiya}"
        return info

    def get_yosh(self, yil=2023):
        return yil - self.t_yil
    
    def set_otasi(self, otasi=''):
        self.__otasi = otasi

    def get_info(self):
        return f"ism: {self.ism}, " \
               f"familiyasi: {self.familiya}, " \
               f"tugilgan yil: {self.t_yil}" \
               f"otasi: {self.__otasi}"


class User(Shaxs):
    count_user = 0

    def __init__(self, ism, familiya, t_yil, email, password):
        super().init(ism, familiya, t_yil)
        self.email = email
        self.password = password
        self.user_count = User.count_user
        User.count_user += 1

    def get_info(self):
        info = super().get_info()
        info += f"Email: {self.email} Password: {self.__password}"
        return info

    def get_validate(self):
        l = len(self.__password)
        if l > 6:
            return "True"
        else:
            f"tugilgan yil: {self.t_yil}"
        return "False"

    def set_password(self, password=''):
        self.__password = password

    @classmethod
    def get_count_user(cls):
        return cls.count_user


class Admin(User):
    count_admin = 0

    def __init__(self, ism, familiya, t_yil, email, password):
        super().init(ism, familiya, t_yil, email, password)
        self.role = 'admin'
        self.admin_count = Admin.count_admin
        Admin.count_admin += 1

    def get_info(self):
        info = super().get_info()
        info += f"Email: {self.email} Password: {self.__password} Role: {self.role}"
        return info

    def ban_user(self):
        return "Foydalanuvchi bloklandi"

    @classmethod
    def get_count_admin(cls):
        return cls.count_admin


user1 = User('Abdulaziz', 'Axmedov', '2001', 'xsssd@ss.c', '12356543')
user2 = User('Abdulaziz2', 'Axmedov2', '2000', 'xsssd@ss.c', '12356543')

print(User.get_count_user())