from .config import client


def create_index(index_name: str):

    """
    Metodo para crear e inicializar un indice para Algolia

    :param index_name: nombre deseado para el index
    :return: el indice para usar en algolia
    """

    return client.init_index(index_name)


def create_dataset(index: object, json: list):
    """
    Crear el conjunto de datos que contendra un indice en algolia

    :param index: indice de algolia
    :param json: lista con uno o mas diccionarios que conformaran el valor(dataset) del indice en
            algolia
    :return: valor del dataset
    """

    return index.add_objects(json)


def verify_index(name: str):
    index_list = client.list_indexes()
    for i in index_list['items']:
        if i['name'] == name:
            return True
    return False
