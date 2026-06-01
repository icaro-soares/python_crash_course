def making_profile(first_name, last_name, **kwargs):
    kwargs['first_name'] = first_name
    kwargs['last_name'] = last_name
    return kwargs

build_profile = making_profile(
        'Ícaro',
        'Calado',
        city='Recife',
        age=30,
        height=1.70
)
print(build_profile)
