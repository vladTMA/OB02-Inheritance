class User:
    def __init__(self, ide: int, name: str, access_level: str):
        self.ide = ide # публичный атрибут
        self.name = name # публичный атрибут
        self.access_level = access_level # публичный атрибут

    def info(self):
        print(f"ID: {self.ide}")
        print(f'Имя {self.name}')
        print(f"Уровень доступа {self.access_level}")
        print("_" * 30)

class UserManager:
    def __init__(self):
        self._users = {} # защищенный

    # Геттер
    def get_users(self):
        return self._users.copy()

    # Сеттер (опционально, если нужно заменить весь словарь)
    def set_users(self, new_users: dict):
        if not isinstance(new_users, dict):
            raise TypeError("Ожидается словарь пользователей")
        self._users = new_users # защищённый атрибут

    def add_user(self, new_user: User):
        if new_user.ide in self._users:
            print(f"Пользователь с ID {new_user.ide} уже существует")
        else:
            self._users[new_user.ide] = new_user
            print(f"Пользователь {new_user.name} добавлен")

    def remove_user(self, user_id: int):
        if user_id in self._users:
            removed = self._users.pop(user_id)
            print(f"Пользователь {removed.name} удалён.")
        else:
            print(f"Пользователь с ID {user_id} не найден.")

    def list_users(self, access_filter: str = None):
        print(f"Список пользователей.")
        for current_user in self._users.values():
            if access_filter is None or current_user.access_level == access_filter:
               current_user.info()

    # Проверяем пользователей - все значения это экземпляры User
    def replace_users(self, new_users: dict):
        if not isinstance(new_users, dict):
            raise TypeError("Ожидается словарь пользователей")
        for uid, user in new_users.items():
            if not isinstance(user, User):
                raise ValueError(f"Элемент с ключом {uid} не является объектом User")
        self._users = new_users

class Admin(User):
        def __init__(self, ide: int, name: str, chef_manager: UserManager):
            super().__init__(ide, name, "Administrator")
            self.__chef_manager = chef_manager # приватный

        # Геттер
        def get_use_manager(self):
            return self.__chef_manager

        # Сеттер
        def set_user_manger(self, new_manager: UserManager):
            if not isinstance(new_manager, UserManager):
                raise TypeError("Ожидвется объект класса UserManager")
            self.__chef_manager = new_manager

        def add_user(self, new_user: User):
            self.__chef_manager.add_user(new_user)

        def remove_user(self, user_id: int):
            self.__chef_manager.remove_user(user_id)

        def list_users(self, access_filter: str = None):
            self.__chef_manager.list_users(access_filter)

# Создание пользователей
user_manager = UserManager()

admin = Admin(1, "БигЧифф", user_manager)
user2 = User(2, "Розалия", "User")
user3 = User(3, "Бобос", "User")
user4 = Admin(4, "Рутер", user_manager)
user5 = User(5, "Гиацинт", "Moderator")

admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)
admin.add_user(user5)

admin.list_users()
admin.remove_user(3)
admin.list_users("User")

# Вывод информации
users = [admin, user2, user3, user4, user5]
for person in users:
    person.info()


