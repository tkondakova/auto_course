class PersonInfo:
    def __init__(self, full_name: str, age: int, *deps):
        self.full_name = full_name
        self.age = age
        self.deps = deps

    def short_name(self):
        """Краткая запись Фамилия И."""
        return self.full_name.split()[1] + ' ' + self.full_name.split()[0][0: 1] + '.'

    def path_deps(self):
        """Путь до подразделения"""
        full_deps = ""
        for i in self.deps:
            full_deps += i + " --> "
        full_deps = full_deps[:-5]
        return (full_deps)

    def new_salary(self):
        """Новая зарплата"""
        #1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
        full_deps_str = ''.join(map(str, self.deps))
        element_count = {}
        for element in full_deps_str:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1
        values = list(element_count.values())
        values.sort(reverse=True)
        return (1337*self.age*(sum(values[:3])))
