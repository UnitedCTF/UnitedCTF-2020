Rails.application.routes.draw do
  root 'invoices#index'

  # Session
  get '/login', to: 'sessions#new'
  post '/login', to: 'sessions#create'
  get '/logout', to: 'sessions#destroy'

  # Users
  resources 'users', only: [:new, :create, :edit, :update]

  # Password reset
  resources 'password_resets', only: [:new, :create, :edit, :update]

  # Invoices
  resources 'invoices', only: [:new, :create, :show, :index]
  get "public/invoices/:public_token", to: "invoices#public", as: :public_invoice

  # Metrics
  get '/metrics', to: 'pages#metrics'

  # Help Center
  get 'help-center', to: 'help_center#home'
  get 'help-center/home', to: 'help_center#home'
  get 'help-center/password_reset', to: 'help_center#password_reset'
  get 'help-center/search_invoice', to: 'help_center#search_invoice'
end
