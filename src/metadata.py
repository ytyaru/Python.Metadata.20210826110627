#!/usr/bin/env python3
# coding: utf8
import os, sys, csv, json, datetime, locale
from string import Template
from collections import namedtuple
class Command:
    def __init__(self, path=None):
        self.__meta = FileReader.json(Path.here('meta.json') if path is None path)
        self.__meta['readme'] = self.__meta['ja']['readme'] if 'ja_JP' == locale.getlocale()[0] else self.__meta['en']['readme']
    @property
    def Version(self): return self.__meta['version'] if self.__meta else '0.0.1'
    @property
    def Summary(self): return self.__meta['readme']['summary'] if self.__meta else 'アクセストークンを返す。'
    @property
    def Details(self): return self.__meta['readme']['details'] if self.__meta else '所定のファイルにトークンを保存しておく。コマンド引数で指定されたドメインとユーザ名で絞り込む。最初に見つかったトークンを返す。見つからなかったらなにも返さない。'
    @property
    def Description(self): return '\n'.join((self.Summary, 
                                            self.Details, 
                                            self.SystemArchitecture, 
                                            '特徴' if 'ja_JP' == locale.getlocale()[0] else 'Features', 
                                            self.Features, 
                                            '注意' if 'ja_JP' == locale.getlocale()[0] else 'Notes', 
                                            self.Notes))
    @property
    def Usage(self): return f'{This.Names.name}{This.Names.ext} DOMAIN USER [SCOPES]...'
    @property
    def Help(self):
        path = os.path.join(This.Names.parent, 'help.txt')
        with open(path, mode='r', encoding='utf-8') as f:
            t = Template(f.read().rstrip('\n'))
            return t.substitute(summary=self.Summary, 
                                usage=self.Usage, 
                                this=f'{This.Names.name}{This.Names.ext}', 
                                version=self.Version,
                                csv=CsvTokenReader().Path)
    @property
    def Meta(self):
        path = os.path.join(This.Names.parent, 'meta.txt')
        with open(path, mode='r', encoding='utf-8') as f:
            t = Template(f.read().rstrip('\n'))
            return t.substitute(description=self.Description, 
                                url=self.Url,
                                license_name=self.License['name'], 
                                license_url=self.License['url'], 
                                since=f'{self.Since:%Y-%m-%dT%H:%M:%S%z}', 
                                copyright=self.Copyright,
                                author_name=self.Author['name'],
                                author_sites='\n'.join(self.Author['sites']))

    @property
    def Since(self):
        return datetime.datetime.fromisoformat(self.__meta['since'] if self.__meta else '2021-08-12T00:00:00+09:00')
    @property
    def Author(self):
        return self.__meta['author'] if self.__meta else {'name': 'ytyaru',
            'sites': [
                'https://github.com/ytyaru',
                'https://twitter.com/ytyaru1',
                'https://mstdn.jp/@ytyaru',
                'https://profile.hatena.ne.jp/ytyaru/'
            ]}
    @property
    def Copyright(self): return f'© {self.Since.year} {self.Author["name"]}'
    @property
    def License(self):
        return self.__meta['license'] if self.__meta else {'name': 'CC0-1.0', 'url': 'https://creativecommons.org/publicdomain/zero/1.0/legalcode'}
    @property
    def Url(self): return self.__meta['url'] if self.__meta else 'https://github.com/ytyaru/Python.AccessToken.20210820093132'
    @property
    def SystemArchitecture(self): return valid(FileReader.text(Path.here('system_architecture.txt')), '''Terminal---------------------------------------+
|    TOKEN                                     |
|      |                                       |
| Python3.7--+                                 |
| | token.py | DOMAIN USERNAME [SCOPE] ...     |
| +----------+                                 |
|      |                                       |
| tokens.tsv---------------------------------+ |
| | domain    username  scopes      token    | |
| | mstdn.jp  ytyaru    read,write  xxxxx... | |
| | ...       ...       ...         ...      | |
| +------------------------------------------+ |
+----------------------------------------------+''')
    @property
    def Features(self):
        text = ''
        if self.__meta and self.__meta['readme']['features']:
            for feature in self.__meta['readme']['features']:
                text += f'* {feature[0]}\n  {feature[1]}\n'
        return text.rstrip('\n')
    @property
    def Notes(self):
        text = ''
        if self.__meta and self.__meta['readme']['notes']:
            for note in self.__meta['readme']['notes']:
                text += f'* {note[0]}\n  {note[1]}\n'
        return text.rstrip('\n')

class Metadata:
    def __init__(self, cmd={}):
        self.__cmd = cmd
    @classmethod
    def call(cls):
        locale.setlocale(locale.LC_ALL, '')
        c_cmds = {
            'description':,
            'features':,
            'notes:,'
            'version:,
        }
        m_cmds = {
            'metadata': {
                'url':,
                'author':,
                'since':,
                'copyright':,
                'license':,
            }
        }
        cmds = []
        cmds.append(['metadata'])
        cmds.append(['url','author','since','copyright','license','description','features','notes'])

