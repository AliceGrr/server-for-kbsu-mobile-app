import os
from server import app
from server.models import Students

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    print(Students.query.all())
    print(Students.get_by_id(2))
    # app.run(port=port, debug=True)
