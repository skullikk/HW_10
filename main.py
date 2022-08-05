from flask import Flask
import functions

def main():

    app = Flask(__name__)
    @app.route('/')
    def page_index():
        candidates = functions.get_all()
        list_candidates = ''
        for candidate in candidates:
            list_candidates += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n'
        return f'<pre>{list_candidates}</pre>'

    @app.route('/candidates/<int:pk>')
    def page_candidates(pk):
        candidate = functions.get_by_pk(pk)
        url = candidate['picture']
        return f"<img src='{url}'>\n\n\
        <pre>Имя кандидата - {candidate['name']}\nПозиция кандидата - {candidate['position']}\nНавыки через запятую - {candidate['skills']}</pre>"

    @app.route('/skills/<skill>')
    def page_skills(skill):
        candidates = functions.get_by_skill(skill)
        list_candidates = ''
        for candidate in candidates:
            list_candidates += f'Имя кандидата - {candidate["name"]}\nПозиция кандидата - {candidate["position"]}\nНавыки через запятую - {candidate["skills"]}\n\n'
        return f'<pre>{list_candidates}</pre>'


    app.run()

if __name__ == '__main__':
    main()