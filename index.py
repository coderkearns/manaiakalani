# Manaiakalani - Maui's magic hook


class Observable:
    def __init__(self, value):
        self._value = value
        self._listeners = []

    def __call__(self):
        return self._value

    def subscribe(self, fn):
        self._listeners.append(fn)
        return lambda: self._listeners.remove(fn)

    # Sets the observable to a new value and triggers all subscribers
    def set(self, value):
        old_value = self._value
        self._value = value

        for fn in self._listeners:
            fn(value, old_value)

    # Mutates the observable's value, then triggers all subscribers
    def mutate(self, mutate_fn):
        mutate_fn(self._value)

        for fn in self._listeners:
            fn(value, old_value)


class Derived(Observable):
    def __init__(self, observables, fn):
        super().__init__(fn())
        if type(observables) is not list:
            observables = [observables]
        self.observables = observables
        self.fn = fn

        self.unsubscribers = [
            o.subscribe(lambda v, ov: super(Derived, self).set(fn()))
            for o in self.observables
        ]

    def set(self, value):
        # Derived cannot be manually set
        pass


# Decorator for creating Derived easily
def derived(observables):
    return lambda fn: Derived(observables, fn)
