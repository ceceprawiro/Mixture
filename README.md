# Mixture
Generate data dummy untuk SQLite menggunakan Flask, SQLAlchemy dan Mixer.

## Persiapan

Lewati tahap ini jika sudah terbiasa dengan Python.

**Install PIP (package manager untuk Python)**

```
$ sudo apt-get install python-pip
```

**Install virtualenv secara global**

```
$ sudo pip install virtualenv
```

## Instalasi Mixture

Clone repository ini ke folder yang diinginkan.

```
git clone https://github.com/ceceprawiro/Mixture.git /path/to/Mixture```

Aktifkan virtualenv untuk folder tersebut.

```
$ virtualenv /path/to/Mixture
$ cd /path/to/Mixture
$ source bin/activate
```

Download package yang dibutuhkan.

```
(Mixture) $ python setup.py install
```

## Jalankan

```
$ python mixture.py
```

Cek hasil outputnya.

```
$ sqlite data.db
sqlite> select * from user;
```

## Links

1. [Flask][Flask]
2. [SQLAlchemy][SQLAlchemy]
3. [Mixer][Mixer]

[Flask]: http://flask.pocoo.org/docs/0.12/
[SQLAlchemy]: http://docs.sqlalchemy.org/en/latest/
[Mixer]: https://mixer.readthedocs.io/en/latest/
