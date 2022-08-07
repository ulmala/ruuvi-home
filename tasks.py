from invoke import task

@task
def init_db(ctx):
    ctx.run('python src/initialize_db.py')