
import json
import os
from models import Estudante, Republica

class PersistenceManager:
    def __init__(self, file_path="user_data.json"):
        self.file_path = file_path

    def load_users(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, "r", encoding="utf-8") as f:
            data_list = json.load(f)

        usuarios = []
        for item in data_list:
            if item["tipo"] == "estudante":
                est = Estudante(
                    item["username"],
                    item["password"],
                    item["nome"],
                    item["telefone"],
                    item["instagram"]
                )
                est.respostas = item.get("respostas", {})
                est.personalidade = item.get("personalidade", {})
                est.perfil_final = item.get("perfil_final", None)
                usuarios.append(est)
            elif item["tipo"] == "republica":
                rep = Republica(
                    item["username"],
                    item["password"],
                    item["nome"],
                    item["telefone"],
                    item["instagram"]
                )
                rep.tipo_escolhido = item.get("tipo_escolhido")
                rep.descricao_tipo = item.get("descricao_tipo")
                usuarios.append(rep)

        return usuarios

    def save_users(self, usuarios):
        data_list = []
        for u in usuarios:
            base_dict = {
                "username": u.username,
                "password": u.password,
                "nome": u.nome,
                "telefone": u.telefone,
                "instagram": u.instagram
            }
            if isinstance(u, Estudante):
                base_dict["tipo"] = "estudante"
                base_dict["respostas"] = u.respostas
                base_dict["personalidade"] = u.personalidade
                base_dict["perfil_final"] = u.perfil_final
            elif isinstance(u, Republica):
                base_dict["tipo"] = "republica"
                base_dict["tipo_escolhido"] = u.tipo_escolhido
                base_dict["descricao_tipo"] = u.descricao_tipo

            data_list.append(base_dict)

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data_list, f, indent=4, ensure_ascii=False)
