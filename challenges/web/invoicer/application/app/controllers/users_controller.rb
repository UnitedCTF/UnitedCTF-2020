class UsersController < ApplicationController
  skip_before_action :authenticate!, only: [:new, :create]

  def new
    return redirect_to '/' if current_user

    @user = User.new

    render :new
  end

  def create
    return redirect_to '/' if current_user
    
    @user = User.new(create_params)
    if @user.save
      flash[:success] = 'Successfully registered.'
      redirect_to login_path
    else
      render :new
    end
  end

  def edit
    @user = current_user

    render :edit
  end

  def update
    @user = current_user
    if @user.demo
      flash[:danger] = 'Forbidden: your account is limited to the basic feature.'
      redirect_to :root
    elsif @user.update(update_params)
      flash[:success] = 'Profile successfully updated.'
      redirect_to :root
    else
      render :edit
    end
  end

  private

  def create_params
    params.require(:user).permit!
  end

  def update_params
    params.require(:user).permit(:name)
  end
end
