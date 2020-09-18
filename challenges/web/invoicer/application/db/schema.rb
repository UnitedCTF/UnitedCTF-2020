# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `rails
# db:schema:load`. When creating a new database, `rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2020_09_18_145937) do

  create_table "invoices", force: :cascade do |t|
    t.integer "amount", null: false
    t.string "details", null: false
    t.string "recipient_email", null: false
    t.string "recipient_name", null: false
    t.string "public_token", null: false
    t.integer "user_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["public_token"], name: "index_invoices_on_public_token", unique: true
    t.index ["user_id"], name: "index_invoices_on_user_id"
  end

  create_table "super_hidden_secret_features", force: :cascade do |t|
    t.string "name", null: false
    t.boolean "hidden", default: true, null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

  create_table "users", force: :cascade do |t|
    t.string "name", null: false
    t.string "email", null: false
    t.string "password_digest", null: false
    t.string "password_reset_token"
    t.datetime "password_reset_generated_at"
    t.boolean "demo", default: true, null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["name"], name: "index_users_on_name", unique: true
    t.index ["password_reset_token"], name: "index_users_on_password_reset_token", unique: true
  end

  add_foreign_key "invoices", "users"
end
