instructions = [
    'DROP TABLE IF EXISTS email;',
    """
    CREATE TABLE email(
        id int primary key auto_increment,
        email text not null,
        subject text not null,
        content text not null
    )
    """
]