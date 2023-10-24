from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать и удалять только свои собственные объекты.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение всем пользователям
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешение на редактирование и удаление только владельцу объекта
        return obj.user == request.user


class IsPublicHabitsList(permissions.BasePermission):
    """
    Пользователи могут видеть список публичных привычек без возможности редактирования и удаления.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return False
