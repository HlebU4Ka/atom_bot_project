from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserList(generics.ListCreateAPIView):
    """
    Список и создание пользователей.

    Это представление позволяет аутентифицированным пользователям просматривать список пользователей и создавать новых.

    Атрибуты:
        queryset (QuerySet): Набор пользователей, которые будут отображаться в списке.
        serializer_class (Serializer): Класс сериализатора для пользователей.
        permission_classes (List[Permission]): Список классов разрешений, необходимых для доступа к этому представлению.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Получение, обновление или удаление пользователя.

    Это представление позволяет аутентифицированным пользователям получать, обновлять и удалять индивидуальных пользователей.

    Атрибуты:
        queryset (QuerySet): Набор пользователей, которые могут быть получены, обновлены или удалены.
        serializer_class (Serializer): Класс сериализатора для пользователей.
        permission_classes (List[Permission]): Список классов разрешений, необходимых для доступа к этому представлению.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]


class UserRegistrationView(generics.CreateAPIView):
    """
    Представление для регистрации новых пользователей.

    Это представление позволяет пользователям отправлять данные для регистрации, включая
    электронную почту, пароль и имя. После успешной регистрации, оно также создает и возвращает токен
    аутентификации для нового пользователя.

    Атрибуты:
        - queryset (QuerySet): Запрос для получения всех пользователей. Не используется в этом представлении.
        - serializer_class (UserRegistrationSerializer): Сериализатор, используемый для обработки данных
          регистрации.
        - permission_classes (list): Список разрешений, в данном случае, AllowAny, разрешает доступ к
          этому представлению без аутентификации.

    Методы:
        create(request, *args, **kwargs): Метод для обработки POST-запросов регистрации новых пользователей.
            Принимает запрос `request` и данные, переданные в теле запроса. Создает сериализатор,
            проверяет валидность данных, создает нового пользователя и возвращает ответ с данными пользователя
            и токеном аутентификации.

    Атрибуты класса:
        - queryset: Запрос для получения всех пользователей.
        - serializer_class: Сериализатор, используемый для обработки данных регистрации.
        - permission_classes: Список разрешений, разрешающих доступ к представлению без аутентификации.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Метод для обработки POST-запросов регистрации новых пользователей.

        Args:
            request (HttpRequest): Объект запроса, содержащий данные пользователя для регистрации.
            *args: Дополнительные позиционные аргументы.
            **kwargs: Дополнительные именованные аргументы.

        Returns:
            Response: Ответ с данными пользователя и токеном аутентификации в случае успешной регистрации.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                'user': UserRegistrationSerializer(user, context=self.get_serializer_context()).data,
                'token': token.key,
            },
            status=status.HTTP_201_CREATED
        )