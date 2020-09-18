class PasswordResetsController < ApplicationController
  skip_before_action :authenticate!, only: [:new, :create, :edit, :update]

  def new
    return redirect_to '/' if current_user

    render :new
  end

  def create
    return redirect_to '/' if current_user

    user = User.find_by(email: params[:email])
    if user && (user.password_reset_generated_at.nil? || user.password_reset_generated_at < 10.minutes.ago)
      user.send_password_reset
    end
    flash[:success] = 'Password reset instruction successfully sent. You can only reset your password every 10 minutes.'
    redirect_to login_path
  end

  def edit
    return redirect_to '/' if current_user

    @user = User.find_by(password_reset_token: params[:id])
    if @user
      if @user.password_reset_generated_at < 1.hour.ago
        flash[:danger] = "Your password reset has expired."
        redirect_to new_password_reset_path
      else
        render :edit
      end
    else
      flash[:danger] = "Invalid password reset token."
      redirect_to login_path
    end
  end

  def update
    return redirect_to '/' if current_user

    @user = User.find_by!(password_reset_token: params[:id])
    if @user.password_reset_generated_at < 1.hour.ago
      flash[:danger] = "Your password reset has expired."
      redirect_to new_password_reset_path
    elsif @user.update(update_params)
      flash[:success] = "Your password has been updated."
      redirect_to login_path
    else
      render :edit
    end
  end

  private

  def update_params
    params.require(:user).permit(:password, :password_confirmation)
  end
end
