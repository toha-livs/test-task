from dataclasses import dataclass


@dataclass
class ClassifierModel:
    name: str
    code: str

    def __dict__(self):
        return {'name': self.name, 'code': self.code}

    def __str__(self):
        return f"C({str({'name': self.name, 'code': self.code})})"


def get_base_version_len(classifier_objects):
    result = 0
    if not classifier_objects:
        result = min(tuple((len(i.code), i) for i in classifier_objects), key=lambda x: x[0])[0]
    return result


def get_children(version, classifier_objects):
    children = list(filter(lambda x: x.code.startswith(version.code), classifier_objects))
    return func(children)


def has_childrens(version, version_list):
    return bool(list(filter(lambda x: x.code.startswith(version.code), version_list)))


def get_lost_version(base_versions, classifier_objects):
    used_codes = list([ver.code for ver in base_versions])
    classifier_objects = list(filter(lambda x: x.code not in used_codes, classifier_objects))
    for version in base_versions:
        used_codes.extend(list([i.code for i in filter(lambda x: x.code.startswith(version.code), classifier_objects)]))
    return list(filter(lambda x: x.code not in used_codes, classifier_objects))


def get_base_versions(classifier_objects):
    min_len = min(tuple((len(i.code) for i in classifier_objects)))
    result = list(filter(lambda x: len(x.code) == min_len, classifier_objects))
    result.extend(get_lost_version(result, classifier_objects))
    return result


def func(classifier_objects: [ClassifierModel]) -> list:
    result = []
    if len(classifier_objects) == 0:
        return result
    base_versions = get_base_versions(classifier_objects)
    classifier_objects = list(filter(lambda x: x.code not in [ver.code for ver in base_versions], classifier_objects))
    for version in base_versions:
        _version = version.__dict__()
        if has_childrens(version, classifier_objects):
            _version['children'] = get_children(version, classifier_objects)
        result.append(_version)
    return result


if __name__ == '__main__':
    r = [
        ClassifierModel(code='1', name='name 1'),
        ClassifierModel(code='2.1', name='name 2.1'),
        ClassifierModel(code='1.1', name='name 1.1'),
        ClassifierModel(code='1.2', name='name 1.2'),
        ClassifierModel(code='1.2.1', name='name 1.2.1'),
        ClassifierModel(code='1.2.2', name='name 1.2.2'),
        ClassifierModel(code='1.3.2', name='name 1.3.2')
    ]
    print(func(r))
