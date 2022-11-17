from anilight.parsers import ShikimoriLib, ShikimoriBase, ShikimoriAnime

CATALOGS = {0: ShikimoriBase}
USER_CATALOGS = [ShikimoriAnime]
LIB_CATALOGS = {ShikimoriBase: ShikimoriLib}


def get_catalog(catalog_id=0):
    return CATALOGS.get(catalog_id)


def get_lib_catalog(base_catalog):
    return LIB_CATALOGS.get(base_catalog)
