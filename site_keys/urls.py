from django.urls import path

from . import views


urlpatterns = [
    path("", views.home_view, name="home"),

    path("keys_shop/", views.keys_shop, name="keys_shop"),

    path(
        "jogo/<int:pk>/",
        views.detalhe_jogo,
        name="detalhe_jogo",
    ),

    # CRUD
    path(
        "jogo/criar/",
        views.criar_jogo,
        name="criar_jogo",
    ),

    path(
        "jogo/<int:pk>/editar/",
        views.editar_jogo,
        name="editar_jogo",
    ),

    path(
        "jogo/<int:pk>/excluir/",
        views.excluir_jogo,
        name="excluir_jogo",
    ),

    # Conta
    path(
        "perfil/",
        views.perfil,
        name="perfil",
    ),

    path(
        "minhas-compras/",
        views.minhas_compras,
        name="minhas_compras",
    ),

    path(
        "configuracoes/",
        views.configuracoes,
        name="configuracoes",
    ),
]