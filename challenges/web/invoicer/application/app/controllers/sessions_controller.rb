class SessionsController < ApplicationController
  skip_before_action :authenticate!, only: [:new, :create]

  def new
    return redirect_to '/' if current_user

    render :new
  end

  def create
    return redirect_to '/' if current_user

    user = User.find_by(email: params[:email])
    if user.try(:authenticate, params[:password])
      flash[:info] = "Welcome back admin | #{ENV['FLAG_1']}" if user.admin?
      session[:user_id] = user.id
      redirect_to '/'
    else
      flash[:danger] = 'Invalid email or password.'
      redirect_to login_path
    end
  end

  def destroy
    flash[:success] = 'Successfully logout.'
    session[:user_id] = nil
    redirect_to login_path
  end
end
