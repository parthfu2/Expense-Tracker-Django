from django.shortcuts import render, redirect
from django.contrib import messages
from tracker.models import *
from django.db.models import Sum


def index(request):
    if request.method == "POST":
        description = request.POST.get("description")
        amount = request.POST.get("amount")

        if not description:
            messages.info(request, "Description Cannot be blank")
            return redirect("/")

        try:
            amount = float(amount)
        except Exception as e:
            messages.info(request, "Amount should be a number")
            return redirect("/")

        # Create the transaction after validation
        Transaction.objects.create(description=description, amount=amount)

        return redirect("/")

    # Get all transactions
    transactions = Transaction.objects.all()

    # Calculate balance, income, and expenses
    total_balance = (
        transactions.aggregate(total_balance=Sum("amount"))["total_balance"] or 0
    )
    income = (
        transactions.filter(amount__gte=0).aggregate(income=Sum("amount"))["income"]
        or 0
    )
    expense = (
        transactions.filter(amount__lte=0).aggregate(expense=Sum("amount"))["expense"]
        or 0
    )

    # Prepare context
    context = {
        "transactions": transactions,
        "balance": total_balance,
        "income": income,
        "expense": expense,
    }

    return render(request, "index.html", context)


def deleteTransaction(request, uuid):
    Transaction.objects.get(uuid=uuid).delete()
    return redirect("/")
