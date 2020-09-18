class InvoicesController < ApplicationController
  skip_before_action :authenticate!, only: [:public]

  def new
    @invoice = current_user.invoices.build
  end

  def create
    if current_user.admin?
      flash[:info] = "#{ENV['SUPPORT_ACCOUNT_NAME']} can not create invoice."
      render :new
      return
    end

    @invoice = current_user.invoices.build(create_params)
    if @invoice.save
      flash[:success] = 'Invoice successfully created and sent.'
      redirect_to invoices_path
    else
      render :new
    end
  end

  def show
    @invoice = current_user.invoices.find(params[:id])

    render :show
  end

  def index
    @invoices = current_user.invoices.all
    if params[:keyword]
      # keyword = "%#{ActiveRecord::Base.sanitize_sql_like(params[:keyword])}%"
      keyword = "%#{params[:keyword]}%"
      @invoices = @invoices.where(
        "(details LIKE '#{keyword}') OR (recipient_name LIKE '#{keyword}') OR (recipient_email LIKE '#{keyword})'"
      )
    end

    render :index
  end

  def public
    @invoice = Invoice.find_by!(public_token: params[:public_token])

    render :public, layout: 'public'
  end

  private

  def create_params
    params.require(:invoice).permit(:amount, :details, :recipient_email, :recipient_name)
  end
end
