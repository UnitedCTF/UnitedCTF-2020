class ApplicationController < ActionController::Base
  before_action :authenticate!

  private

  def authenticate!
    unless current_user
      flash[:danger] = 'You must be authenticated to access this page.'
      redirect_to login_path
    end
  end

  def current_user
    @current_user ||= User.find(session[:user_id]) if session[:user_id]
  end

  helper_method :current_user
end
