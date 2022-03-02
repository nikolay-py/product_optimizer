from webapp.recipes.models import Recipe


def test_recipes_endpoint_post(test_client):
    # create_product(
    #     client.db,
    #     name='test',
    #     link_photo='link',
    #     price=100,
    #     description='test desc',
    #     category='test-category',
    # )
    # url = 'https://menunedeli.ru/recipe/rzhanye-drozhzhevye-bliny/'
    # url = 'https://menunedeli.ru/recipe/omlet-na-paru/'
    # url = 'https://menunedeli.ru/recipe/domashnyaya-tortilya-ispanskaya-lepeshka/'
    url = 'https://menunedeli.ru/recipe/faxitos-s-kuricej-i-ovoshhami/'
    # url = 'https://menunedeli.ru/recipe/kapustnyak-s-tykvoj/'
    res = test_client.post('/', data={'url': url})
    recipes = test_client.db.session.query(Recipe).filter_by(url=url).first()

    assert isinstance(recipes.id, int)
    assert isinstance(recipes.name, str)
    assert isinstance(recipes.url, str)
    assert isinstance(recipes.product_list, list)
    assert isinstance(recipes.product_list[0], dict)

    assert res.status_code == 200
