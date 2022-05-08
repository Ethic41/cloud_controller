"""initialized database

Revision ID: 49d23dc745c0
Revises: 
Create Date: 2022-05-08 14:52:29.933781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49d23dc745c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_groups_created_at'), 'groups', ['created_at'], unique=False)
    op.create_table('passwordresets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_passwordresets_created_at'), 'passwordresets', ['created_at'], unique=False)
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_permissions_created_at'), 'permissions', ['created_at'], unique=False)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_roles_created_at'), 'roles', ['created_at'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('last_modified', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('old_password_hash', sa.String(length=255), nullable=True),
    sa.Column('firstname', sa.String(length=255), nullable=True),
    sa.Column('lastname', sa.String(length=255), nullable=True),
    sa.Column('middlename', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_system_user', sa.Boolean(), server_default='0', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_users_created_at'), 'users', ['created_at'], unique=False)
    op.create_table('permission_role',
    sa.Column('permission_id', sa.String(length=50), nullable=True),
    sa.Column('role_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['permissions.uuid'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.uuid'], )
    )
    op.create_table('role_group',
    sa.Column('role_id', sa.String(length=50), nullable=True),
    sa.Column('group_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.uuid'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.uuid'], )
    )
    op.create_table('user_group',
    sa.Column('group_id', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['groups.uuid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.uuid'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_group')
    op.drop_table('role_group')
    op.drop_table('permission_role')
    op.drop_index(op.f('ix_users_created_at'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_roles_created_at'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_permissions_created_at'), table_name='permissions')
    op.drop_table('permissions')
    op.drop_index(op.f('ix_passwordresets_created_at'), table_name='passwordresets')
    op.drop_table('passwordresets')
    op.drop_index(op.f('ix_groups_created_at'), table_name='groups')
    op.drop_table('groups')
    # ### end Alembic commands ###
