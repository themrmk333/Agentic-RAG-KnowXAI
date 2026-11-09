"""Add biometric_credentials table and user oauth fields.

Revision ID: 0003_biometric_credentials
Revises: 0002_vector_dim_384
Create Date: 2026-10-17
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa

revision = "0003_biometric_credentials"
down_revision = "0002_vector_dim_384"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1. Add google_id and auth_provider columns to users table
    op.add_column("users", sa.Column("google_id", sa.String(length=255), nullable=True))
    op.add_column("users", sa.Column("auth_provider", sa.String(length=32), server_default="local", nullable=False))
    op.create_index("ix_users_google_id", "users", ["google_id"], unique=True)

    # 2. Create biometric_credentials table
    op.create_table(
        "biometric_credentials",
        sa.Column("id", sa.Integer(), primary_key=True, index=True),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            unique=True,
            nullable=False,
            index=True,
        ),
        sa.Column("encrypted_template", sa.Text(), nullable=False),
        sa.Column("template_version", sa.String(length=64), server_default="v1_mobilenet_512d", nullable=False),
        sa.Column("is_enabled", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.Column("enrolled_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("last_used_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("failed_attempts", sa.Integer(), server_default="0", nullable=False),
        sa.Column("locked_until", sa.DateTime(timezone=True), nullable=True),
    )


def downgrade() -> None:
    op.drop_table("biometric_credentials")
    op.drop_index("ix_users_google_id", table_name="users")
    op.drop_column("users", "auth_provider")
    op.drop_column("users", "google_id")
